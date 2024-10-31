import { DoBootstrap, Injector, NgModule } from '@angular/core';
import { WebcamProgramNodeComponent } from './components/webcam-program-node/webcam-program-node.component';
import { WebcamApplicationNodeComponent } from './components/webcam-application-node/webcam-application-node.component';
import { UIAngularComponentsModule } from '@universal-robots/ui-angular-components';
import { BrowserModule } from '@angular/platform-browser';
import { createCustomElement } from '@angular/elements';
import { HttpBackend, HttpClientModule } from '@angular/common/http';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import {MultiTranslateHttpLoader} from 'ngx-translate-multi-http-loader';
import { PATH } from '../generated/contribution-constants';
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import { WebcamModule } from 'ngx-webcam';

export const httpLoaderFactory = (http: HttpBackend) =>
    new MultiTranslateHttpLoader(http, [
        { prefix: PATH + '/assets/i18n/', suffix: '.json' },
        { prefix: './ui/assets/i18n/', suffix: '.json' },
    ]);

@NgModule({
    declarations: [
        WebcamProgramNodeComponent,
        WebcamApplicationNodeComponent
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        UIAngularComponentsModule,
        HttpClientModule,
        WebcamModule,
        TranslateModule.forRoot({
            loader: { provide: TranslateLoader, useFactory: httpLoaderFactory, deps: [HttpBackend] },
            useDefaultLang: false,
        })
    ],
    providers: [],
})

export class AppModule implements DoBootstrap {
    constructor(private injector: Injector) {
    }

    ngDoBootstrap() {
        const webcamprogramnodeComponent = createCustomElement(WebcamProgramNodeComponent, {injector: this.injector});
        customElements.define('urcaps-r-us-simple-webcam-webcam-program-node', webcamprogramnodeComponent);
        const webcamapplicationnodeComponent = createCustomElement(WebcamApplicationNodeComponent, {injector: this.injector});
        customElements.define('urcaps-r-us-simple-webcam-webcam-application-node', webcamapplicationnodeComponent);
    }

    // This function is never called, because we don't want to actually use the workers, just tell webpack about them
    registerWorkersWithWebPack() {
        new Worker(new URL('./components/webcam-application-node/webcam-application-node.behavior.worker.ts'
            /* webpackChunkName: "webcam-application-node.worker" */, import.meta.url), {
            name: 'webcam-application-node',
            type: 'module'
        });
        new Worker(new URL('./components/webcam-program-node/webcam-program-node.behavior.worker.ts'
            /* webpackChunkName: "webcam-program-node.worker" */, import.meta.url), {
            name: 'webcam-program-node',
            type: 'module'
        });
    }
}

