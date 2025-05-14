import {Component, inject, OnInit} from '@angular/core';
import {Store} from '@ngxs/store';
import {SetSetting} from '../../modules/settings/settings.actions';
import {Observable} from 'rxjs';
import {BaseComponent} from '../../components/base/base.component';
import {takeUntil, tap} from 'rxjs/operators';
import {TranslocoService} from '@jsverse/transloco';
import {TranslationService} from '../../modules/translate/translate.service';
import {Meta, Title} from '@angular/platform-browser';
import {MediaMatcher} from '@angular/cdk/layout';
import {TranslateMobileComponent} from './translate-mobile/translate-mobile.component';
import {TranslateDesktopComponent} from './translate-desktop/translate-desktop.component';

@Component({
  selector: 'app-translate',
  templateUrl: './translate.component.html',
  styleUrls: ['./translate.component.scss'],
  imports: [TranslateMobileComponent, TranslateDesktopComponent],
})
export class TranslateComponent extends BaseComponent implements OnInit {
  private store = inject(Store);
  private transloco = inject(TranslocoService);
  translation = inject(TranslationService);
  private mediaMatcher = inject(MediaMatcher);
  private meta = inject(Meta);
  private title = inject(Title);

  isMobile: MediaQueryList;

  constructor() {
    super();
    this.isMobile = this.mediaMatcher.matchMedia('screen and (max-width: 599px)');

    // Default settings for text-to-sign only
    this.store.dispatch([
      new SetSetting('drawSignWriting', true),
      new SetSetting('drawPose', true),
      new SetSetting('poseViewer', 'pose'),
    ]);
  }

  ngOnInit(): void {
    this.transloco.events$
      .pipe(
        tap(() => {
          this.title.setTitle(this.transloco.translate('translate.title'));
          this.meta.updateTag(
            {
              name: 'description',
              content: this.transloco.translate('translate.description'),
            },
            'name=description'
          );
        }),
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe();
  }
}
