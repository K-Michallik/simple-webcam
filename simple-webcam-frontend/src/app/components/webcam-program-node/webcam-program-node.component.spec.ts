import {ComponentFixture, TestBed} from '@angular/core/testing';
import {WebcamProgramNodeComponent} from "./webcam-program-node.component";
import {TranslateLoader, TranslateModule} from "@ngx-translate/core";
import {Observable, of} from "rxjs";

describe('WebcamProgramNodeComponent', () => {
  let fixture: ComponentFixture<WebcamProgramNodeComponent>;
  let component: WebcamProgramNodeComponent;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WebcamProgramNodeComponent],
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

    fixture = TestBed.createComponent(WebcamProgramNodeComponent);
    component = fixture.componentInstance;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
