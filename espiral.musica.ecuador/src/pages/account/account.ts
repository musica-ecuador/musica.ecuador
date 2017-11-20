import { Component,OnInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { UserLoginPage } from '../user-login/user-login';

import { UserDataService }    from '../../providers/user-data/user-data';


/**
 * Generated class for the AccountPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-account',
  templateUrl: 'account.html',
})
export class AccountPage implements OnInit  {

  user: any;

  constructor(public navCtrl: NavController, public navParams: NavParams,
    public userDataService: UserDataService) {
  }


  ngOnInit(): void {
    this.userDataService.hasLoggedIn().then(value => 
      {
        if (value === true){
          
          this.userDataService.getUserLogged().then(
          
            user => this.user = user
          
          );

        }else{
          this.user = null;
          this.navCtrl.setRoot(UserLoginPage);
        }
      }
    );
  }
  

  ionViewDidLoad() {
    console.log('ionViewDidLoad AccountPage');
  }

}
