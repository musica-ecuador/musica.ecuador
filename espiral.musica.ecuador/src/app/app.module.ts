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
import { ListPage } from '../pages/list/list';
import { ArtistPage } from '../pages/Artist/artist';
import { AlbumPage } from '../pages/album/album'
import { TrackPage } from '../pages/track/track'
import { VideoPage } from '../pages/video/video'


import { ArtistService } from '../providers/artist/artist';
import { AlbumService } from '../providers/album/album';
import { TrackService } from '../providers/track/track';
//import { YoutubeService } from '../providers/youtube/youtube';

import { DurationAudioPipe } from '../pipes/duration-audio/duration-audio'

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    AboutPage,
    ContactPage,
    ListPage,
    ArtistPage,
    AlbumPage,
    TrackPage,
    VideoPage,
    DurationAudioPipe
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    AboutPage,
    ContactPage,
    ListPage,
    ArtistPage,
    AlbumPage,
    TrackPage,
    VideoPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    ArtistService,
    AlbumService,
    TrackService,
    //YoutubeService
  ]
})
export class AppModule {}
