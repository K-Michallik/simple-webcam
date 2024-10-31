import { ApplicationNode } from '@universal-robots/contribution-api';

export interface WebcamApplicationNodeNode extends ApplicationNode {
  type: string;
  version: string;
}
