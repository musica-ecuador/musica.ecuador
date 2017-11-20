import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';

import { HttpModule }    from '@angular/http';


import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';

import { MyApp } from './app.component';

import { HomePage } from '../pages/home/home';
import { AboutPage } from '../pages/about/about';
import { ContactPage } from '../pages/contact/contact';
//import { ListPage } from '../pages/list/list';
import { ArtistPage } from '../pages/Artist/artist';
import { AlbumPage } from '../pages/album/album'
import { TrackPage } from '../pages/track/track'
import { VideoPage } from '../pages/video/video'
import { YoutubePage } from '../pages/youtube/youtube'
import { SearchLabPage } from '../pages/search-lab/search-lab'
import { UserSignupPage }  from '../pages/user-signup/user-signup';
import { UserLoginPage } from '../pages/user-login/user-login';
import { AccountPage } from '../pages/account/account';

import { ArtistService } from '../providers/artist/artist';
import { AlbumService } from '../providers/album/album';
import { TrackService } from '../providers/track/track';
//import { YoutubeService } from '../providers/youtube/youtube';
import { YoutubeService } from '../providers/youtube/youtube';
import { UserDataService } from '../providers/user-data/user-data';


import { DurationAudioPipe } from '../pipes/duration-audio/duration-audio';
import { YoutubePipe } from '../pipes/youtube/youtube';


import { YoutubeVideoPlayer } from '@ionic-native/youtube-video-player';


import { IonicStorageModule } from '@ionic/storage';

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    AboutPage,
    ContactPage,
    //ListPage,
    ArtistPage,
    AlbumPage,
    TrackPage,
    VideoPage,
    YoutubePage,
    SearchLabPage,
    UserSignupPage,
    UserLoginPage,
    AccountPage,

    DurationAudioPipe,
    YoutubePipe
    
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule,
    IonicStorageModule.forRoot()
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    AboutPage,
    ContactPage,
    //ListPage,
    ArtistPage,
    AlbumPage,
    TrackPage,
    VideoPage,
    YoutubePage,
    SearchLabPage,
    UserSignupPage,
    UserLoginPage,
    AccountPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    ArtistService,
    AlbumService,
    TrackService,
    YoutubeService,
    YoutubeVideoPlayer,
    UserDataService
    //{provide: Window, useValue: window}
  ]
})
export class AppModule {}
