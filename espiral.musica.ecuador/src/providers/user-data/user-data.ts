import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

import { AppSettings } from "../../app/settings";
import { Storage } from '@ionic/storage';
import { Console } from '@angular/core/src/console';


/*
  Generated class for the UserDataProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class UserDataService {

  HAS_LOGGED_IN = 'hasLoggedIn';
  USER = 'user';

  url: string = AppSettings.PARSE_SERVER + '/parse/users';
  url_login: string = AppSettings.PARSE_SERVER + '/parse/login';
  url_logout: string = AppSettings.PARSE_SERVER + '/parse/logout';

  private headers: Headers = new Headers();


  constructor(public http: Http, public storage: Storage) {
    this.headers.append('Content-Type', 'application/json');
    this.headers.append('X-Parse-Application-Id', AppSettings.PARSE_APPLICATION_ID);
  }

  hasLoggedIn(): Promise<boolean> {
    return this.storage.get(this.HAS_LOGGED_IN).then((value) => {
      return value === true;
    });
  };

  getUserLogged(): Promise<any> {

    return this.storage.get(this.USER).then((value) => {
      return value;
    });

  };


  login(username: string, password: string): Promise<any> {

    //let params = "username=" + JSON.stringify(username)+ "&password="+ JSON.stringify(password) ;
    let params = "username=" + username.trim() + "&password=" + password.trim();
    let urlFinal = this.url_login + "?" + params;

    return this.http.get(urlFinal, { headers: this.headers })
      .toPromise()
      .then(response => {
        let data = response.json();
        this.storage.set(this.HAS_LOGGED_IN, true);
        this.storage.set(this.USER, data);
        return data;
      }
      )
      .catch(this.handleError);
  };


  signup(username: string, password: string): Promise<any> {

    let data = {
      "username": username,
      "password": password
    };


    let urlFinal = this.url;

    return this.http.post(urlFinal, data, { headers: this.headers })
      .toPromise()
      .then(response => response.json())
      .catch(this.handleError);
  };

  logout(): Promise<boolean> {

    console.log('logout..');

    //TODO: Promise chain
    return this.hasLoggedIn().then(value => {

      if (value === true) {
        return this.getUserLogged().then(user => {

          let headers_custom: Headers = new Headers();

          headers_custom.append('Content-Type', 'application/json');
          headers_custom.append('X-Parse-Application-Id', AppSettings.PARSE_APPLICATION_ID);
          headers_custom.append('X-Parse-Session-Token', user.sessionToken);

          let urlFinal = this.url_logout;

          return this.http.post(urlFinal, {}, { headers: headers_custom })
            .toPromise()
            .then(response => {

              this.storage.remove(this.HAS_LOGGED_IN);
              this.storage.remove(this.USER);
              console.log('logout ok');
              return true;

            })
            .catch(this.handleError);
        }
        );
      } else {
        return true;
      }
    });



  };


  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
