import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { NgForm } from '@angular/forms';

import {UserOptions } from '../../interfaces/user-options';
import { UserDataService }    from '../../providers/user-data/user-data';

import { UserSignupPage } from '../user-signup/user-signup';
import { AccountPage  } from '../account/account';


/**
 * Generated class for the UserLoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-user-login',
  templateUrl: 'user-login.html',
})
export class UserLoginPage {

  login: UserOptions = { username: '', password: '' };
  submitted = false;

  constructor(public navCtrl: NavController, public navParams: NavParams,
    public userDataService: UserDataService) {
  }

  onLogin(form: NgForm) {
    this.submitted = true;

    if (form.valid) {
      
      this.userDataService.login(this.login.username,this.login.password)
        .then(
          data => {
            console.log(data);
            //this.navCtrl.push(AccountPage);
            this.navCtrl.setRoot(AccountPage);
          }
        );
    }
  }

  onSignup() {
    this.navCtrl.push(UserSignupPage);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UserLoginPage');
  }

}
