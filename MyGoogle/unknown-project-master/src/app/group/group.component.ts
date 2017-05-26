import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {GapiService} from '../services/gapi.service'

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.scss']
})
export class GroupComponent implements OnInit, OnDestroy {

  id: string;
  private sub: any;

  constructor(private route: ActivatedRoute, private gapiService: GapiService) {
  }

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.gapiService.loadGroup(params['id']).then(data => {
        console.log(data.result);
      })
    });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
