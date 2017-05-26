import {Component, NgZone, OnInit} from '@angular/core';
import {GapiService} from '../services/gapi.service'

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  myGroups: any;
  me: any;

  constructor(ngZone: NgZone, private gapiService: GapiService) {
    this.myGroups = [];
    this.me = {};
    window['onSignIn'] = (user) => ngZone.run(() => this.onSignIn(user));
  }

  public onSignIn(googleUser) {
    // this.me = googleUser;
    const profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail());
    this.me = {name: profile.getName(), photo: profile.getImageUrl()};
    this.gapiService.loadClient().then(() => {
      this.gapiService.initPersonalGroups(profile.getEmail(), profile.getEmail()).then(
        data => {
          console.log(data);
          this.myGroups = data.result.stat_block.filter(item => item.group_name !== 'General parametrs');
          console.log(this.myGroups);
        }
      );
    });
  }

  ngOnInit() {
  }
}
