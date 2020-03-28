/* Hello World */

const sayHello = (name?: String) => {
  console.log(`Hello ${name || "World"} !`);
};

sayHello();
sayHello("Simon");

/* Entretien */

const countNumber = (input: Array<number>) => {
  const result: any = {};
  input.forEach(nb => {
    if (!result[nb]) {
      result[nb] = 1;
    } else {
      result[nb]++;
    }
  });
  console.log(result);
};

countNumber([1, 1, 3, 4, 5, 5, 5]);

import { Observable } from "rxjs";

let cpt = 0;
const myObservable = new Observable(subscriber => {
  subscriber.next(cpt++);
});

myObservable.subscribe(c => {
  console.log(c);
});

myObservable.subscribe(d => {
  console.log(d);
});

import { from } from "rxjs";

const arrayObservable = from([10, 20, 30]);

arrayObservable.subscribe(d => {
  console.log(`arrayObservable ${d}`);
});

import { of } from "rxjs";
import { map } from "rxjs/operators";

map((nb: number) => nb * nb)(of(1, 2, 3)).subscribe(v =>
  console.log(`value: ${v}`)
);

import { filter } from "rxjs/operators";

arrayObservable
  .pipe(
    filter(v => !(v % 2)),
    map(v => v + v)
  )
  .subscribe(v => console.log(`value pipe: ${v}`));

import { interval } from "rxjs";
