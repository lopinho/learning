import {
  UseInterceptors,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';

import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { plainToClass } from 'class-transformer';

interface ClassConstructor {
  new (...args: any[]);
}

export function Serialize(dto: ClassConstructor) {
  return UseInterceptors(new SerializerInterceptor(dto));
}

export class SerializerInterceptor implements NestInterceptor {
  constructor(private dto: ClassConstructor) {}

  intercept(context: ExecutionContext, handler: CallHandler): Observable<any> {
    // run before a request is handled
    return handler.handle().pipe(
      map((data: any) => {
        // run before response is sent response
        return plainToClass(this.dto, data, { excludeExtraneousValues: true });
      }),
    );
  }
}
