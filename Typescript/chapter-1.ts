// Type Annotation

let full_name: String = "Dzakiy";
let age: Number = 23;
let is_married: Boolean = false;

let anything: any = "it can be string";
anything = 10;

// Array type Annotation
let fruits: String[] = ["Apple", "Banana", "Melon"];

// Object type Annotation
let person: {
  full_name: String;
  age: Number;
  is_married: Boolean;
} = {
  full_name: "Dzakiy",
  age: 21,
  is_married: false,
};

//  Type Alliases

type newType = number | string;

let new_variable: newType = 20;

new_variable = "20";

interface Person {
  full_name: string;
  age: Number;
  is_married: Boolean;
}

let person_2: Person = {
  full_name: "Dzakwan",
  age: 22,
  is_married: true,
};

let someValue: any = "This is a variable with any type";
let strLength: number = (someValue as string).length;

// Generi type

type ApiResponse<T> = {
  status: number;
  message: string;
  data: T;
};
