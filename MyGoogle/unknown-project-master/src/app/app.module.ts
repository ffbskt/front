import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {RouterModule, Routes} from '@angular/router';
import {AppComponent} from './app.component';
import {GroupComponent} from './group/group.component';
import {GroupsComponent} from './groups/groups.component';
import {HeaderComponent} from './header/header.component';
import {ProfileComponent} from './profile/profile.component';
import {SearchBoxComponent} from './search-box/search-box.component';
import {GroupsService} from './groups/groups.service';
import {GroupSearchPipe} from './groups/group-search.pipe';
import {GapiService} from './services/gapi.service';
import {LoginService} from './services/login.service';
import {CapitalizePipe} from './pipes/capitalize.pipe';


const routes: Routes = [
  {path: 'group/:id', component: GroupComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'groups', component: GroupsComponent},
  {path: '', redirectTo: '/profile', pathMatch: 'full'},
];

@NgModule({
  declarations: [
    AppComponent,
    GroupComponent,
    GroupsComponent,
    HeaderComponent,
    ProfileComponent,
    SearchBoxComponent,
    GroupSearchPipe,
    CapitalizePipe,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(routes)
  ],
  providers: [GroupsService, GapiService, LoginService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
