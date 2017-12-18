import { Component,ViewChild } from '@angular/core';

import { FORM } from './form';


 
import FormioUtils from 'formiojs/utils';


import { FormioComponent } from 'angular-formio/formio.component';

import { Parse } from 'parse';
Parse.initialize("123");
Parse.serverURL = 'http://localhost:1337/parse'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  private form: any = FORM; 
  
  @ViewChild('formRender') formRender: FormioComponent;

  private options: any = {
    hooks: {
      
      beforeSubmit: (submission: any, callback: any) => {
        console.log('Before Submit');
        console.log(submission);
   
        var Client = Parse.Object.extend("Client");
        var client = new Client();
        
        this.mapObjectToParse(client,submission.data);
       
        //save obj parse
        client.save(null, {

          success: function(client) {
            // Execute any logic that should take place after the object is saved.
            console.log('New object created with objectId: ' + client.id);
            submission.data.id =  client.id;
            callback(null, submission)

          },
          error: function(client, error) {

            //TODO: Buscar una mejor forma, capturar el evento de Error.
            this.enableButton();

            // Execute any logic that should take place if the save fails.
            // error is a Parse.Error with an error code and message.
            callback(error, submission)
            console.log('Failed to create new object, with error code: ' + error.message);
          }
        });
 
      }

    }
  };


  mapObjectToParse(objParse:any, source:any) {
    
    for (var prop in source) {
      if( source.hasOwnProperty(prop) ) {
        var value = source[prop];
        if (value){
          objParse.set(prop, value);
        }
      } 
    }              
  }
  
  showObject(obj:any) {
    var result = "";
    for (var p in obj) {
      if( obj.hasOwnProperty(p) ) {
        var value = obj[p];
        if (value)
          result += p + " , " + obj[p] + "\n";
      } 
    }              
    console.log( result);
  }

  onInvalid(error:any){
    console.log('onInvalid');
    console.log(error);
  }

  onError(err: any) {
    console.log('onError');
    console.log(err);
  }

  onSubmit(submission: any) {
    
    console.log(submission); // This will print out the full submission from Form.io API.

    this.enableButton();

  }

  enableButton(){
    
    if (!this.formRender)
      return;

    let comps = FormioUtils.findComponents(this.formRender.formio.components, {
      'type': 'button',
      'component.action':'submit'
    });

    if (comps){
      comps[0].loading = false;
      comps[0].disabled =false;
    }
  }

  onRender() {
    console.log('onRender');
  }
  
}
