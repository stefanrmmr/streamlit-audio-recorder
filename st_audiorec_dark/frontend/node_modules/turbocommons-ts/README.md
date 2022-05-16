### General purpose cross-language development library

Devs around the world do the same things every day with different languages. They perform string modifications, validations, data conversions, file operations and more.

Why must they learn new ways of doing the same thing every time they move to a new language?

TurboCommons tries to standardize all those common operations so they are performed the same way across all possible languages. It is a library that uses the same methods and classes across all the implemented languages.

### Documentation

**A detailed code specification is available online. You can check it [here](https://turbocommons.org)**

### How to use it

- Php:
```
Currently available only as a .phar file (download it from https://turbocommons.org)
require '..../turbocommons-php-X.X.X.phar';
use org\turbocommons\src\main\php\utils\StringUtils;
$n = StringUtils::countWords("word1 word2 word3");
```
- Typescript:
```
npm install turbocommons-ts
import { StringUtils } from 'turbocommons-ts';
let n = StringUtils.countWords("word1 word2 word3");
```
- Javascript 5:
```
npm install turbocommons-es5
<script src="turbocommons-es5/turbocommons-es5.js"></script>
var StringUtils = org_turbocommons.StringUtils;
var n = StringUtils.countWords("word1 word2 word3");
```
- Javascript 6:
```
npm install turbocommons-es6
<script src="turbocommons-es6/turbocommons-es6.js"></script>
var StringUtils = org_turbocommons.StringUtils;
var n = StringUtils.countWords("word1 word2 word3");
```
- NodeJS projects:
```
npm install turbocommons-ts
const {StringUtils} = require('turbocommons-ts');
var n = StringUtils.countWords("word1 word2 word3");
```

### Language support

- Php (7 or more recommended)
- Typescript
- Javascript 5
- Javascript 6

We want to increase this list. So! if you want to translate the library to your language of choice, please contact us! We need your help to port this library to as many languages as possible, and more important, we need to code the SAME unit tests across all the implemented languages. This is the only way to guarantee that the library delivers exactly the same behavior everywhere.

### Dependencies

The main goal for this library is to have zero dependencies. We are building a true standalone general purpose library.

### Contribute

Turbo Commons is 100% free and open source, but we will be really pleased to receive any help, support, comments or donations to help us improve this library. If you like it, spread the word!

- You can get more info at the official site:

	- [turbocommons.org](https://turbocommons.org)

### Donate
	
[![Donate](https://turbocommons.org/view/views/home/donate-button.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=53MJ6SY66WZZ2&lc=ES&item_name=TurboCommons&no_note=0&cn=A%c3%b1adir%20instrucciones%20especiales%20para%20el%20vendedor%3a&no_shipping=2&currency_code=EUR&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)
