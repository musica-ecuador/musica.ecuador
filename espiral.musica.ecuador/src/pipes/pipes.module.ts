import { NgModule } from '@angular/core';
import { DurationAudioPipe } from './duration-audio/duration-audio';
import { YoutubePipe } from './youtube/youtube';
@NgModule({
	declarations: [DurationAudioPipe,
    YoutubePipe],
	imports: [],
	exports: [DurationAudioPipe,
    YoutubePipe]
})
export class PipesModule {}
