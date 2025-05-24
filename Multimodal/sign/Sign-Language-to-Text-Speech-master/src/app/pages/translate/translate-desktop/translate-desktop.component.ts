import {Component, inject} from '@angular/core';
import {BaseComponent} from '../../../components/base/base.component';
import {IonButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar} from '@ionic/angular/standalone';
import {LanguageSelectorsComponent} from '../language-selectors/language-selectors.component';
import {SendFeedbackComponent} from '../send-feedback/send-feedback.component';
import {TranslocoPipe} from '@jsverse/transloco';
import {NtkmeButtonModule} from '@ctrl/ngx-github-buttons';
import {SpokenToSignedComponent} from '../spoken-to-signed/spoken-to-signed.component';
import {addIcons} from 'ionicons';
import {language} from 'ionicons/icons';
import {RouterLink} from '@angular/router';
import {LogoComponent} from '../../../components/logo/logo.component';

@Component({
  selector: 'app-translate-desktop',
  templateUrl: './translate-desktop.component.html',
  styleUrls: ['./translate-desktop.component.scss'],
  imports: [
    IonHeader,
    IonToolbar,
    IonButtons,
    IonContent,
    IonTitle,
    LanguageSelectorsComponent,
    SendFeedbackComponent,
    TranslocoPipe,
    SpokenToSignedComponent,
    LogoComponent,
  ],
})
export class TranslateDesktopComponent extends BaseComponent {
  constructor() {
    super();
    addIcons({language});
  }
}
