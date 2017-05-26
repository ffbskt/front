import {Injectable} from '@angular/core';
import {Http, Response} from '@angular/http';
import {Groups} from './groups';

import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

@Injectable()
export class GroupsService {
  private url = 'https://graphgroop.appspot.com/_ah/api/rrrq/v1/all_group';

  constructor(private http: Http) {
  }

  getGroups(): Observable<any> {
    return this.http.get(this.url)
      .map((response: Response) => response.json())
      .catch(this.handleError);
  }

  private handleError(error: any) {
    console.log(error);
    return Observable.throw(error);
  }
}
