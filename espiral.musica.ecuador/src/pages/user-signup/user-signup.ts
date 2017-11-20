import { Component,OnInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { NgForm } from '@angular/forms';

import { LoadingController } from 'ionic-angular';

import { UserLoginPage } from '../user-login/user-login';

import {UserOptions } from '../../interfaces/user-options';
import { UserDataService }    from '../../providers/user-data/user-data';


/**
 * Generated class for the UserSignupPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-user-signup',
  templateUrl: 'user-signup.html',
})
export class UserSignupPage implements OnInit  {
  
  loading:any;
  

  user : any;

  signup: UserOptions = { username: '', password: '' };
  submitted = false;

  constructor(public navCtrl: NavController,
     public navParams: NavParams,
     public loadingCtrl: LoadingController,
     public userDataService: UserDataService) {

    

  }

  ngOnInit(): void {
    
        this.loading = this.loadingCtrl.create({
          content: 'Por favor espere...'
        });

  }

  onSignup(form: NgForm) {
    
    this.submitted = true;

    if (form.valid) {
      
      this.loading.present();

      this.userDataService.signup(this.signup.username,this.signup.password)
        .then(
          data => {
            this.user = data;
            console.log(this.user);
          
            this.loading.dismissAll();

            this.navCtrl.setRoot(UserLoginPage);
          }
        );
    }
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UserSignupPage');
  }

}
