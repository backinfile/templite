from templite import Templite
template = r"""

    This template demonstrates the usage of Templite.

    Within the defined delimiters we can write pure Python code:

    ${
        def say_hello(name):
            write('Hello %s!' % name)
    }$

    And now we call the function: ${ say_hello('World') }$

    Escaped starting delimiter: $\{
    ${ write('Escaped ending delimiter: }\$') }$

    Also block statements are possible:

    ${ if x > 10: }$
    x is greater than 10
    ${ :elif x > 5: }$
    x is greater than 5
    ${ :else: }$
    x is not greater than 5
    ${ :end-if / only the starting colon is essential to close a block }$

    ${ for i in range(x): }$
    loop index is ${ i }$
    ${ :end-for }$

    ${ # this is a python comment }$

    Single variables and expressions starting with quotes are substituted
    automatically:
    Instead ${write(x)}$ you can write ${x}$ or ${'%s' % x}$ or ${"", x}$
    Therefore standalone statements like break, continue or pass
    must be enlosed by a semicolon: $\{continue;}\$

    To include another template, just call "include":
    $\{ include('template.txt') }\$
    """
t = Templite(template)
print(t.render(x=5))