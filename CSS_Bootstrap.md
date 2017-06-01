# CSS и Bootstrap

Согласно Википедии: 
> CSS (англ. Cascading Style Sheets — каскадные таблицы стилей) — формальный язык описания внешнего вида документа, написанного с использованием языка разметки.
Преимущественно используется как средство описания, оформления внешнего вида веб-страниц, написанных с помощью языков разметки
HTML и XHTML, но может также применяться к любым XML-документам, например, к SVG или XUL.

Cодержимое страницы описывается в специальном файле на специальном языке разметки - HTML, 
а внешний вид этой страницы может храниться в другом специальном файле и описываться на специальном языке -  CSS.

CSS уместно использовать, когда мы делаем сайт, у которого больше одной страницы или на единственной странице сайта 
больше шести элементов. В современном мире CSS нужен всегда, когда речь заходит о фронтэнде.

## Как добавить CSS-описание к странице?
1)  CSS можно прописывать прямо в теле страницы: внутри HTML

          <html>
          <head>
          <style type="text/css">*ТУТ CSS КОД*</style>
          </head>
          <body>*ТУТ КОД СТРАНИЦЫ*</body>
          </html>
          
2) но лучше это делать в отдельном файле с расширением .css и вставить ссылку на этот файл внутри HTML

          <head>
          <link rel="stylesheet" type="text/css" href="сюда нужно вставить путь к файлу .css">
          </head>

## Синтаксис

          element {
          property1 : value1;
          property2 : value1 value2 value3;
          }
          element2 {
          property3 : value4;
          property4 : value5 value6;
          }
          
Например:

          p {
          color : blue;
          font-size: 70%;
          }
          h1 {
          font-size: 50px;
          }

         
## Как это применять?

При помощи CSS можно менять оформление всех элементов, которые пишутся в угловых скобках. 

А также отдельные классы элементов (см. ниже - Классы и идентификаторы). 

Ещё можно задать стиль всего сразу, написав звёздочку (*) вместо названия элемента.

При помощи CSS можно задавать значения отдельным параметрам элементов: расположение элементов и контента внутри элементов, цвета, размеры, шрифты, форму элементов, границы элементов и т.д.

### Расположение элементов
Параметр `position`
* `absolute` — положение элемента определяется относительно границ родительского элемента (если у родительского элемента `position : static`, то относительно окна браузера)
* `fixed` — как `absolute`, только при прокрутке элемент остаётся на месте.
* `relative` — положение элемента определяется относительно того, где бы он располагался по дефолту.
* `static` — элемент расположен там, где должен быть по дефолту, и нельзя сдвинуть.

Параметры расположения элементов
* `margin` - Определяет положение элемента относительно границ родителя.
* `padding` - Определяет расстояние от краёв элемента до контента внутри.
* `width` - Определяет ширину элемента.
* Если нужно подвинуть что-то относительно одного края, то используется `margin-top`, `margin-left`, `padding-right` и т.д.
 
![margin vs padding](https://i.stack.imgur.com/A6YUp.png)


### Цвета
* `color` отвечает за цвет текста
* `background-color` — за цвет фона впределах элемента.
* Цвета принято указывать в формате HEX — код цвета выглядит как `#00bfff`.
* Если элемент должен быть прозрачным или полупрозрачным, цвет указывается в формате `rgba(258, 258, 258, 0.5)`, где первые три числа — описание цвета в RGB, последнее — степень
прозрачности. `0` — полностью прозрачный, `1` — полностью непрозрачный.

Цвета можно подбирать здесь - http://websafecolors.info.


### Шрифт
* `font-family` — имя шрифта или хотя бы указание на то, с засечками он (`serif`) или без (`sans-serif`).
* `font-size` — размер шрифта. Указывается в `pt`, `em`, `px`, процентах.
* `font-style` — выбор между обычным шрифтом (`normal`), курсивом (`italic`) и наклонным шрифтом (`oblique`).
* `font-weight` — жирный (`bold`), значение по умолчанию (`normal`), менее жирный, чем по умолчанию (`lighter`).
* `text-decoration` – подчёркивание (`underline`), надчёркивание (`overline`), зачёркивание (`line-through`), мигающий текст (`blink`).

### Границы
* `border-radius` — радиус скругления углов границ элемента;
указывается в px.
* `border-color` — цвет границы элемента.
* `border-style` — стиль границы (`dotted`, `dashed`, `solid` и другие).
* `border-width` — толщина границы, указывается в `px`.

### Классы и идентификаторы
Для элементов html-страницы можно задавать классы и `id`, например, `<p class="name_of_class">` или `<div id="chart">`. Классам и идентификаторам можно присваивать свои стили.

В CSS классы указываем через точку, а идентификаторы через решетку:

          .name_of_class {
          property1 : value1;
          property2 : value1 value2 value3;
          }
          #chart {
          property1 : value1;
          property2 : value1 value2 value3;
          }

Если у элемента есть и класс, и id, и их стили конфликтуют, то будет отображаться стиль id.

Можно указывать класс каких именно элементов мы описываем:

          p.name_of_class {
          property1 : value1;
          property2 : value1 value2 value3;
          }
          div#chart {
          property1 : value1;
          property2 : value1 value2 value3;
          }


Можно давать одному элементу несколько классов `<p class="name_of_class special_paragraph">` и задавать стиль мультиклассами:

          .name_of_class.special_paragraph {
          property1 : value1;
          property2 : value1 value2 value3;
          }
		  
Стиль мультикласса применится только к тем элементам, у которых есть оба класса.

### Селекторы
Вложенные селекторы: Задаём стиль тех элементов `p`, которые находятся внутри `div`.(`<div><p>...</p></div>`) 

          div p {
          property1 : value1;
          property2 : value1 value2 value3;
          }
		  

Дочерние селекторы: Задаём стиль тех элементов `p`, которые являются непосредственным ребенком `div`. (`<div><p>...</p></div>`, но не `div><span><p>...</p></span></div>`)

          div > p {
          property1 : value1;
          property2 : value1 value2 value3;
          }
		  

### Псевдоклассы
`:first-child`, `:nth-child`, `:last-child`, `:nth-last-child`, `only-child`

Задаём стиль четвёртой "дочки" элемента `p`. Вместо числа можно писать `odd`, `even`.

          p:nth-child[4] {
          property1 : value1;
          property2 : value1 value2 value3;
          }
		  
		  
Псевдоклассы ссылок. 
* `:link` — для ссылок, по которым пользователь ещё не проходил, 
* `:hover` — стиль ссылки (или любого другого элемента) при наведении на неё курсора, 
* `:visited` — для посещённых ссылок.

          a:hover {
          property1 : value1;
          property2 : value1 value2 value3;
          }
		  

### Пример
Используя только CSS и немного фантазии можно делать очень красивые вещи. Например, можно нарисовать красивую кнопку.

HTML:

			<span class="bigprettybutton">Кнопка</span>

CSS:

			.bigprettybutton {
				background-color: transparent;
				border: 3px solid rgba(3,14,148,.98);
				padding: 2px 3px;
				border-radius: 10px;
				color: rgba(3,14,148,.98);
				font-size: 1.0em;
				font-weight: 600;
				opacity: .9;
				margin-bottom: 0;
				cursor: pointer
			}

## Ссылки
* htmlbook.ru — большой русскоязычный словарь HTML и CSS.
* w3schools.com — "The world’s largest web developer site"


## Bootstrap
Снова с Википедии:
> Bootstrap (также известен как Twitter Bootstrap) — свободный набор инструментов для создания сайтов и веб-приложений. Включает в себя HTML- и CSS-шаблоны оформления для типографики, веб-форм, кнопок, меток, блоков навигации и прочих компонентов веб-интерфейса, включая JavaScript-расширения. Bootstrap использует современные наработки в области CSS и HTML, поэтому необходимо быть внимательным при поддержке старых браузеров.

Иными словами, Bootstrap позволяет нам не писать свои CSS стили, а применить уже готовые к своей странице.

Бутстрап -- это хорошо, потому что:
* стили уже готовы, не нужно ничего придумывать,
* хорошо выглядит на всех браузерах,
* хорошо выглядит на смартфонах (если правильно использовать), планшетах и компьютерах.

Страница [Bootstrap](http://getbootstrap.com/getting-started/) в интернете содержит вообще все, что вам нужно для его использования. 

Чтобы начать им пользоваться, нужно скачать основные файлы (`.css` и `.js`) с сайта и прописать ссылку к ним в вашем `html`. Или же можно ничего не скачивать, а просто вставить вот эти ссылки в `<head>` вашей страницы:

			<!-- Latest compiled and minified CSS -->
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

			<!-- Optional theme -->
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

			<!-- Latest compiled and minified JavaScript -->
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
			

Базовые примеры:
* http://getbootstrap.com/getting-started/#template 
* http://getbootstrap.com/getting-started/#examples 

В основе лежит идея представлять страницу в виде сетки и раскладывать элементы по этой сетке. [Сетка Bootstrap]():

![сетка](http://prideparrot.com/Source-Codes/Images/bootstrap/bootstrap-grid.png)

Структура страницы выглядит примерно так:

			<div class="row">
			  <div class="col-*-*"></div>
			</div>
			<div class="row">
			  <div class="col-*-*"></div>
			  <div class="col-*-*"></div>
			  <div class="col-*-*"></div>
			</div>
			<div class="row">
			  ...
			</div>

Например, у нас может быть ряд с тремя колонками:

			<div class="row">
			  <div class="col-sm-4">.col-sm-4</div>
			  <div class="col-sm-4">.col-sm-4</div>
			  <div class="col-sm-4">.col-sm-4</div>
			</div>
			

В [компоненты Bootstrap](http://getbootstrap.com/components/) входят стили для кнопок, иконок, навигационных панелей на сайте, значки, панели и т.д. Описание каждого компонента лучше смотреть на сайте.
			
Кроме Bootstrap есть и другие фреймворки, например:
* Изящный Skeleton- http://getskeleton.com/
* И очень популярный Material Design - http://www.getmdl.io/ + иконки https://design.google.com/icons/
