import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'groupSearch'
})
export class GroupSearchPipe implements PipeTransform {

  transform(value: any, args?: any): any {
    return null;
  }

}
