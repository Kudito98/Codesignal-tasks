<p>As a professional and respected database programmer, you implemented a low-level API for your front-end colleagues to use. One of them, however, appeared to be quite an ungrateful exemplar, and had the nerve to criticize your work: it seems to him that the functionality your API provides is too basic, and he has to implement several additional functions on his end to make things work.</p>
<p>You don't like to leave the users of your ingenious work disgruntled, so you have to update your API. It can be done quite simple: most of the high-level functionality can be added by combining several basic functions. Now you need to implement a function that will compose an arbitrary number of <code>functions</code>, and test it on some variable <code>x</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]</code><br />
and <code>x = 3.1415</code>, the output should be<br />
<code>solution(functions, x) = 1</code>.</p>
<p><code>abs(math.sin(3 * 3.1415 / 2)) = abs(sin(4.71225)) ≈ abs(-1) = 1</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string functions</strong></p>
<p>Array of functions. Each function is given as a string. It is guaranteed that the result of applying function <code>eval</code> to <code>functions[i]</code> produces a valid function for each <code>i</code>. It is also guaranteed that <code>functions[0](functions[1](functions[2](...(functions[functions.length - 1])...)))</code> is defined in point <code>x</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ functions.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] float x</strong></p>
<p>The value to which the functions should be applied. It is guaranteed that it contains at most <code>4</code> digits after the decimal point.</p>
<p><em>Guaranteed constraints:</em><br />
<code>-1000 ≤ x ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] float</strong></p>
<p>The value obtained by applying composition of <code>functions</code> to <code>x</code>. Your output will be considered correct if its absolute error does not exceed <code>10<sup>-5</sup></code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
