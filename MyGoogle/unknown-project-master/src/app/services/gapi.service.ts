import {Injectable} from '@angular/core';
declare let gapi: any;
@Injectable()
export class GapiService {

  constructor() {
  }

  loadClient(): Promise<any> {
    return new Promise(resolve => {
      console.log(gapi);
      gapi.client.load('rrrq', 'v1', null, 'https://graphgroop.appspot.com/_ah/api')
        .then(resolve);
    });
  }

  initPersonalGroups(whom, tmail): Promise<any> {
    return new Promise(resolve => {
      gapi.client.rrrq.show_user({
        'whom_show': whom,
        'tmail_this': tmail
      }).then(resolve);
    });
  }

  loadGroup(url): Promise<any> {
    return new Promise(resolve => {
      gapi.client.rrrq.show_group({
        group_url: url,
      }).then(resolve);
    });
  }
}
