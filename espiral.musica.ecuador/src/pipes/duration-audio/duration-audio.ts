import { Pipe, PipeTransform } from '@angular/core';

/**
 * Generated class for the DurationAudioPipe pipe.
 *
 * See https://angular.io/api/core/Pipe for more info on Angular Pipes.
 */
@Pipe({
  name: 'durationAudio',
})
export class DurationAudioPipe implements PipeTransform {
 
  /**
   * Takes a value in milliseconds to string minutes and seconds
   */
  transform(ms: number) : string {

    let min = Math.floor((ms/1000/60) << 0);
    let sec = Math.floor((ms/1000) % 60);
    return min + ':' + sec;

  }
}
