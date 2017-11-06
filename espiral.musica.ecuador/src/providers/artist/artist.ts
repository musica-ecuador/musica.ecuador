import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';


/*
  Generated class for the ArtistProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ArtistService {

  url: string = 'http://localhost:1337/parse/classes/Artist';
  private headers: Headers = new Headers();
 
  constructor(public http: Http) {
    this.headers.append('Content-Type', 'application/json');
    this.headers.append('X-Parse-Application-Id', '123');
    console.log('Hello ArtistProvider Provider');
  }

 
  get(id:string): Promise<any> {
    let query = {"objectId":id};
    let where = "where="+JSON.stringify(query);
    let urlFinal = this.url + "?"+where;

    return this.http.get(urlFinal,{headers: this.headers})
    .toPromise()
    .then(response => response.json().results)
    .catch(this.handleError);
  }
  
  findAll(): Promise<any[]> {

    //TODO: Get artist exist field spotify
    let query = {"spotify":{"$exists":"true"}};
    let where = "where="+JSON.stringify(query);
    let urlFinal = this.url + "?limit=500&order=name&"+where;

     return this.http.get(urlFinal,{headers: this.headers})
         .toPromise()
         .then(response => response.json().results)
         .catch(this.handleError);
  }
 
  

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

 

}
