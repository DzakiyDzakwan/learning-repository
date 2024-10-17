# Typescript

Typescrip is a typed superset of Javascript that compiles to Javascript. Typescript is a strict type language which mean if you declare some variable with String type, you only allow to fill the variable with string

## Installation

### Pre-Requisite :

1. Node JS version 16 upper

### How to install Typescript :

1. Install Typescript globally using npm, if you want install typescript only for the project you can delete `-g` command

```
npm install -g typescript
```

2. Check if typescript has been installed

```
tsc --version
```

or

```
tsc -v
```

3. Ini the typescript project

```
tsc -init
```

### How to compile typescript

```
tsc <name_file>.ts
```

Typescript will compile the file into javascript file

## Data Type

1. Number: Represents numeric values (integers and floating-point numbers).
2. String: Represents textual data.
3. Boolean: Represents true or false values.
4. null: Represents the absence of a value.
5. undefined: Represents a variable that has not been assigned a value.
6. any: Represents a value of any type. It's generally used when you're unsure about the type or want to avoid type checking.
7. never: Represents a type that never returns a value (e.g., functions that always throw exceptions).

### Type Annotation

1. Variable

```
 let <variable_name> : <type> = <value>
```

array data type

```
let <variable_name> : <type>[] = [<value1>, <value2>]
```

object data type

```
let <variable_name> : {
    <key1> : <type>,
    <key2> : <type>,
} = {
    <key1> : <value1>,
    <key2> : <value2>
}
```

Function parameter data type

```
let <function_name> = (<parameter1>:<type>) => {
    // Expression here
}
```

#### Type Alliases

We can make our own type like this

```
type <type_name> = <type>
```

example :

```
type stringAndNumber = string | number

let string_number: stringAndNumber = "this variable can be string or number"
```

#### Interfaces

Interface define a contract for an object, specifying its properties and their types. Interface is primarily used to define the structure of objects

```
interface Employee {
  readonly userId: EmployeeId;
  name: string;
  email: string;
}

let employee: Employee = {
  employeeId: 1,
  name: "Bambang",
  email: "bambang@gmail.com",
};
```

##### Extending Interface

```
interface Employee {
  readonly userId: EmployeeId;
  name: string;
  email: string;
}

interface MarketingEmployee extends Employee {
    posititon: string;
}
```

##### Class Interface

```
interface Vehicle {
  make: string;
  model: string;
  year: number;
  drive(): void;
}

class Car implements Vehicle {
  constructor(make: string, model: string, year: number) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  drive() {
    console.log("Driving  
 a car.");
  }
}

class Motorcycle implements Vehicle {
  constructor(make: string, model: string, year: number) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  drive() {
    console.log("Driving  
 a motorcycle.");
  }
}
```

### Type Assertion

`as` keyword is used for type assertions, allowing you to explicitly inform the compiler about the type of a value when it cannot be inferred automatically. Type assertions are a way to override the default static type-checking behavior and tell the compiler that you know more about the type of a particular expression than it does.

```
let someValue: any = "Hello, TypeScript!";
let strLength: number = (someValue as string).length;
```
