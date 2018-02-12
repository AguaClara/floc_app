# AguaClara Interactive Tutorial
The aim of this interactive tutorial is to get you acclimated to working out of a Markdown, or `.md`, file. Markdown is a markup language with plain text formatting that has a lot of functionality. Some of the benefits of working out of markdown include the ability to write text, create charts, write functioning code in a whole bunch of languages, and render LaTeX equations. Markdown gives you all the functionality of a Jupyter Notebook. Despite this, there isn't a clean way to directly convert a `.ipynb` file to a `.md` file, meaning there's no way to easily convert between the two files.

This tutorial will go over how to write in Markdown, how to code in Python, how to run your code using Hydrogen, and how to use Teletype and GitHub in Atom.

# How To View This Markdown File
To view this file in a nice format, press `Cntrl + Shift + M` in Atom. You should now see a preview window that shows what the source code looks like when it's formatted. **(Note: All the interactive parts of this tutorial need to be completed in the source code format.)**

# How To Modify This Markdown File Without Changing It For Others
Because this tutorial exists on a repository that all of AguaClara can access, any change that you make in this file will make that change for all other members after you `commit` and `push`. In order to avoid this, you should make a personal GitHub repository, clone it to your local drive, and copy this file into it. To make a personal repository, go to the [GitHub website](https://github.com). Click on the green `New repository` button, and create a repository named "Personal", and clone it using Atom. **(Note: This repository should not exist within the AguaClara GitHub organization, but rather should be tied to your personal account)**.

Alternatively, if you're a GitHub expert, you can modify this file without changing it for others by forking the `aguaclara_tutorial` repository. **(Note: Only attempt this if you really know what you're doing)**.

You can find a GitHub tutorial [here](https://github.com/AguaClara/aguaclara_tutorial/wiki/Tutorial:-GitHub-Basics) to go over anything related to GitHub.

# Writing and Formatting in Markdown
 Writing in Markdown is very easy. When writing in a `.md` file, unformatted text in source code translates to regular text, just like any word processor.

1. Below this, write a sentence or two about yourself:

<!--- Fill you answer here. --->




## Headers
To signify a header, use `#`. The more `#` you use, the smaller the header gets. For example, the following header Markdown code gets translated as such:

```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

1. Make a header of similar size as Header 3 with whatever text you want:

<!--- Fill you answer here. --->

## Emphasis
There are several different ways to emphasize text: *italics*, **bold**, ***combined***, and ~~strikethrough~~.

* To get *italics*, your italicized text should be enclose in single asterisks as such: `*Italics*`
* To get **bold**, your bolded text should be enclosed in double asterisks as such: `**Bold**`
* To get ***combined***, your text should be enclosed in triple asterisks as such: `***Combined***`
* To get ~~strikethrough~~, your text should be enclosed in double tildes as such `~~strikethrough~~`

1. Write 4 of your favorite words using each type of emphasis:

<!--- Fill you answer here. --->


## Lists
Lists are very easy to do. For a bulleted list, use the asterisk and for a numbered list, use the number followed by a period. Hitting `Enter` after a bullet or number continues the list automatically. Hitting `Enter` followed by `Tab` gets you a sub item for a bulleted list. For example:

1. This is a numbered list
* This is a bulleted list
  - This is a sub-item in a bulleted list

1. Now try it out for yourself. Write down a list of things you hope to achieve this semester, and elaborate on them with sub items:

<!--- Fill you answer here. --->

## Images
To input images, you'll either need an image URL or a file path to your image. For AguaClara work, your repository should have a folder for images where you can get an image URL or file path from. In this tutorial, I've made an image folder with a picture in the `aguaclara_tutorial` repository.

To get your image URL, go to your GitHub repository on your web browser and navigate to the file where your image is stored. Click on the image name, and it should pop up. Right click on the image, and copy image address to get it's URL. **(Note: You should never copy the URL to the folder where the image is stored in the repository.)**

![CopyImageAddress](https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/CopyImageAddress.png)

When you're trying to insert an image that's stored in a folder in the same repository as your Markdown file, you can use a relative file path to that image to insert it rather than using a URL. For example, the relative file path for the Cornell seal image you see in here is `/Images/Cornell_University_seal.svg.png`. Notice how the first part of the path is the folder within this repository where I store my images, and the second part is the image file name and extension.

There are several ways to import an image.
* You can import an image unformatted by using this source code `![Some_Description_of_the_Image](YOUR IMAGE URL or /path/to/image.ext)`
* You can also import an image that's formatted for size using this source code `<img src="YOUR IMAGE URL" height=a width=b>`
  - You have the option to modify both the image height and width or only one if you desire
  - If you modify only one of them, the image will not distort
  - If you modify both, your image may distort

Unformatted Image:

Using a URL:
![CornellSeal](https://github.com/AguaClara/aguaclara_tutorial/blob/master/Images/Cornell_University_seal.svg.png?raw=true)

Using a Relative File Path:
![CornellSeal](/Images/Cornell_University_seal.svg.png)

Image with Height and Width Adjusted:

<img src="https://github.com/AguaClara/aguaclara_tutorial/blob/master/Images/Cornell_University_seal.svg.png?raw=true" height=200 width=100>

1. Make an images folder in your personal repository, and import an image of your hometown or pet from that folder. Do it unformatted using the image URL and the relative file path method, then do it again but instead change the height and width of your image:

<!--- Fill you answer here. --->





## Links
You can also link text to a webpage. For example, I've inserted a link [here](http://aguaclara.cee.cornell.edu) to the AguaClara website.

To insert a link, all you have to do is enclose your linked text in `[]` followed immediately by `()` with no space between them. Your URL goes in the parentheses. It should look like this `[Text_to_be_Linked](URL)`.

1. Below, write a sentence describing your major, and insert a link to your major's department website.

<!--- Fill you answer here. --->

## Tables
Tables in Markdown are slightly harder, but there's an automatic function that allows to you make one easily. When working in a `.md` file, all you have to do is type `table` and hit enter. It will initialize a 2 by 2 table, but you can easily increase the width by going to the last column and hitting `Tab` or it's height by clicking in any cell and hitting `Enter`. Notice in the example how the text below the header is justified left, center, and right. This is due to the line below the header. A line with a colon on the far left of the dashes only indicates left justified, colons on both sides of the dashes indicates centered, and a colon on the far right of the dashes indicates right justified.

```
| Column 1 | Column 2 | Column 3 |
|:-------- |:--------:| --------:|
| 1        |    2     |        3 |
```

| Column 1 | Column 2 | Column 3 |
|:-------- |:--------:| --------:|
| 1        |    2     |        3 |

When making tables, it's not important that the lines match up. For example, the following table code will still give you a nice table:

```
| Column 1 | Column 2 | Column 3 |
|:--------    |:--------:|----:|
| 1        |         2     |             3 |
```

| Column 1 | Column 2 | Column 3 |
|:--------    |:--------:|----:|
| 1        |         2     |             3 |


1. Create a table listing your 3 favorite animals, foods, books, and places on campus. Try out the different cell justifications:

<!--- Fill you answer here. --->



## Code and Syntax Highlighting
Notice how throughout this document there have been computer and programming related words formatted to look more "computery". That's because I've used syntax highlighting.

Syntax highlighting is a great way to emphasize and point out commands, single lines of code, or file types. Basically anything in a paragraph that's related to coding or computer syntax should be syntax highlighted. To do this, use a back tick around your word, phrase, or line. For example, I want to show the Python print function in syntax highlighting as such: `print('Welcome to My Tutorial!')`.

For larger code blocks where you report multiple lines of code, you always start with triple back ticks. If you know you want to write in Python, you would follow your triple back ticks with the word "python". **Note: Python must be lowercase after the back ticks**. To end your code block, you would put down another set of triple back ticks on the line following the last line of code.

~~~~
```python
# Your code goes here
```
~~~~

1. Below, write a Python print function with a different string using syntax highlighting:

<!--- Fill you answer here. --->

2. Now write a block of Python code for that same print statement:

<!--- Fill you answer here. --->



## LaTeX Equations
You can also input LaTeX formatted equations in your Markdown file. To indicate where your equation is, you need to start and end your LaTeX equation with `$$`. To get the LaTeX preview to show it formatted, press `Cntrl + Shift + X`. For example, toggle the LaTeX preview for the line below:

$$ Re_D = \frac{uD}{\nu} $$

1. Try it on your own! Write your favorite equation using LaTeX source code and toggle the LaTeX preview to see it formatted:

<!--- Fill you answer here. --->


# Using Python and Running it With Hydrogen in Markdown

## Running Code With Hydrogen
1. Below this, I've copied the code I wrote for the [Python Basics Tutorial](https://github.com/AguaClara/aguaclara_tutorial/wiki/Tutorial:-Python-Basics). You should familiarize yourself with the different Hydrogen commands using this code. For the first line, use `Hydrogen: Run` (`Cmnd + Enter`).
2. For the second line, use `Hydrogen: Run and Move Down` (`Shift + Enter`).
3. For the remaining code, highlight it with your cursor and use `Hydrogen: Run`. What is the difference between the three?

```python
from aide_design.play import*

xArray = u.Quantity(np.arange(0.1, 0.5, 0.01), u.m)

@u.wraps(None, [u.m / u.s, u.m, u.m ** 2 / u.s], False)
def re_flat_plate(velocity, dist, nu):
  """This function calculates the Reynolds Number for flow past a plate using fluid velocity, plate length, and kinematic viscosity."""
  return (velocity * dist / nu)

plt.plot(xArray, 5 * xArray / np.sqrt(re_flat_plate(1, xArray, pc.viscosity_kinematic(293 * u.kelvin))), '-', label = 'Blasius Solution')
plt.xlabel('Distance From Leading Edge (Meters)')
plt.ylabel('Boundary Layer Thickness (Meters)')
plt.title('Blasius Solution for Water at 293 K')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.legend(loc = 'lower right', ncol = 1)
plt.show()
```

## Python Basics
These questions are meant to test what you've learned from the Python Basics tutorial. If you need help answering a question, refer there first and use other online resources before seeking a Subteam Lead or RA. Be sure to run all your code with Hydrogen. When you code, make sure your using proper [variable naming](https://github.com/AguaClara/aide_design/wiki/Variable-Naming) and [coding standards](https://github.com/AguaClara/aide_design/wiki/Standards)

1. Write a conditional statement with 3 conditions: when x is 10, when x is 1, and when x is anything other than 1 or 10. For each condition, have your code print what the value is or isn't.

<!--- Fill you answer here. --->




2. Write a `for` loop that takes a variable with an initial value of 0, and adds the current index to the previous value of that variable (i.e. you variable should grow in size every iteration). Perform the iteration 20 times, and have the final value be printed at the end.

<!--- Fill you answer here. --->









3. Using the NumPy package, calculate the value of sin(4), and use the sigfig function from the utility module in aide_design to get your answer to 3 sig-figs. *(Hint: You will need to import these packages. Remember how to do that?)*

<!--- Fill you answer here. --->



4. Create a `list` of length 5, and verify the length of your list. Once you've done that, turn your `list` into an `array` and apply units of meters to it. After that, create a 5x5 `array`, extract the middle row and middle column. Verify the size of your 2D `array` and apply units of liters to it.

<!--- Fill you answer here. --->









5.  One of the most famous equations for a particle diffusing through a liquid at low Reynolds Number is the Stokes-Einstein Equation where k<sub>B</sub> is the Boltzmann constant, T is the temperature in Kelvin, eta is the dynamic viscosity in kg/(m*s), and r is the particle radius. Write a function that takes a temperature in Kelvin, a particle radius in meters, and a viscosity of water to calculate the diffusion coefficient D.

    Since this requires the Boltzmann Constant from SciPy, I've started the code for you with an import. Add a function call at the end of your code block and put some numbers into the inputs. Run your code with Hydrogen.

    *(Hint: You'll want to make sure Temperature input is turned into Kelvin and radius input is turned into meters. Your answer should also be in base units How might you do this? Check back to the Python Basics tutorial where I wrote an Ideal Gas function)*

$$ D = \frac{k_BT}{6\pi\eta r} $$

```python
from scipy.constants import Boltzmann as kB_sc # I've imported the unitless value for kB from SciPy

kB = kB_sc * u.joule / u.kelvin # I've given kB units for you in J/K; you can use the kB variable to give you Boltzmann's constant with units

# Write your code here

```

6. You have a pipe with a radius of 0.2 m with water flowing in it at 2 m<sup>3</sup>/s. You want to see how the Reynolds Number changes as viscosity changes due to a change in temperature from 0 to 200<sup>o</sup>C. Create a plot of Reynolds Number against Temperature in Kelvin to show a relationship. Make sure your plot has a title, labeled axes, and axes grid. You can use functions from `physchem` like `pc.re_pipe` and `pc.viscosity_kinematic`. *(Hint: Make an array of temperatures to input into the `pc.viscosity_kinematic` function)*. Make sure to save your plot to your images folder in your personal repository, and display it below using `plt.show()` and an image insertion using a relative file path to the image.

<!--- Fill you answer here. --->

# Teletype Basics
In this section you and your team can practice using Teletype together.

1. Create a portal for your team members to join. Have them write you words of  encouragement in the space below, and be sure they sign their name next to their encouragements.

<!--- Fill you answer here. --->




2. Have you other team members create a portal for you to join. In their Markdown file, write them something encouraging, and sign your name.

<!--- Fill you answer here. --->


# GitHub Basics
Congratulations! You've completed this interactive tutorial. Now all you need to do is save your work and put it on your personal repository. Toggle the Git Tab using `Cntrl + Shift + 9`.

1. Stage your changes.
2. In your commit message write that you've completed the tutorial.
3. Commit your changes and push them.
