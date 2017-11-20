import { Component, ViewChild } from '@angular/core';
import { Nav, Platform } from 'ionic-angular';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { HomePage } from '../pages/home/home';
import { AboutPage } from '../pages/about/about';
//import { ListPage } from '../pages/list/list';
import { ArtistPage } from '../pages/Artist/artist';
import { ContactPage } from '../pages/contact/contact';
import { VideoPage } from '../pages/video/video';
import { YoutubePage } from '../pages/youtube/youtube'
import { SearchLabPage } from '../pages/search-lab/search-lab'
import { UserSignupPage } from '../pages/user-signup/user-signup';
import { UserLoginPage } from '../pages/user-login/user-login';

import { UserDataService } from '../providers/user-data/user-data';
import { AccountPage } from '../pages/account/account';



@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  
  @ViewChild(Nav) nav: Nav;

  
  rootPage:any = HomePage;

  pages: Array<{title: string, component: any, icon: string, logsOut?: boolean}>;

  
  constructor(public  platform: Platform,
    public  statusBar: StatusBar, 
    public  splashScreen: SplashScreen,
    public userDataService: UserDataService) {

    this.initializeApp();

     // used for an example of ngFor and navigation
     this.pages = [
      { title: 'Inicio', component: HomePage, icon:'home' },
      //{ title: 'Listas', component: ListPage,icon:'list' },
      { title: 'Artistas', component: ArtistPage,icon:'musical-notes' },
      { title: 'Video', component: VideoPage,icon:'list' },
      { title: 'Youtube', component: YoutubePage,icon:'list' },
      { title: 'Busqueda-Labs', component: SearchLabPage,icon:'list' },
      { title: 'Registrar Usuario', component: UserSignupPage,icon:'log-out' },
      { title: 'Ingresar', component: UserLoginPage,icon:'list' },
      { title: 'Salir', component: HomePage,icon:'list', logsOut: true },
      { title: 'Perfil', component:AccountPage, icon:'contact'},
      { title: 'Contacto', component:ContactPage, icon:'contact'},
      { title: 'Acerca', component: AboutPage,icon:'information-circle' },
    ];

    

  }

  initializeApp() {
    this.platform.ready().then(() => {
      console.log('platform.ready...');
      
      // Okay, so the platform is ready and our plugins are available.
  

      //This code loads the IFrame Player API code asynchronously.
      console.log('Add youtube...');
     
      var tag = document.createElement('script');
      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
      

      // Here you can do any higher level native things you might need.
      this.statusBar.styleDefault();
      this.splashScreen.hide();

    });
  }

  openPage(page) {
    // Reset the content nav to have just this page
    // we wouldn't want the back button to show in this scenario
    this.nav.setRoot(page.component);

    if (page.logsOut === true) {
      // Give the menu time to close before changing to logged out
      this.userDataService.logout();
    }

  }
}

