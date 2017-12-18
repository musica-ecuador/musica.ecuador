import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';


import { FormioModule } from 'angular-formio';
import { LabsComponent } from './labs/labs.component';


@NgModule({
  declarations: [
    AppComponent,
    LabsComponent
  ],
  imports: [
    BrowserModule,
    FormioModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
