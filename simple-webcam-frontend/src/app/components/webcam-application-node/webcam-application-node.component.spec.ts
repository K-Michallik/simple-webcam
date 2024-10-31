import {ComponentFixture, TestBed} from '@angular/core/testing';
import {WebcamApplicationNodeComponent} from "./webcam-application-node.component";
import {TranslateLoader, TranslateModule} from "@ngx-translate/core";
import {Observable, of} from "rxjs";

describe('WebcamApplicationNodeComponent', () => {
  let fixture: ComponentFixture<WebcamApplicationNodeComponent>;
  let component: WebcamApplicationNodeComponent;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WebcamApplicationNodeComponent],
      imports: [TranslateModule.forRoot({
        loader: {
          provide: TranslateLoader, useValue: {
            getTranslation(): Observable<Record<string, string>> {
              return of({});
            }
          }
        }
      })],
    }).compileComponents();

    fixture = TestBed.createComponent(WebcamApplicationNodeComponent);
    component = fixture.componentInstance;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
