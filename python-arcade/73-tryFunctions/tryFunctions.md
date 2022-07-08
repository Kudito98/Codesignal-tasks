<p>You've been working on a numerical analysis when something went horribly wrong: your solution returned completely unexpected results. It looks like you apply a wrong function at some point of calculation. This part of the program was implemented by your colleague who didn't follow the PEP standards, so it's extremely difficult to comprehend.</p>
<p>To understand what function is applied to <code>x</code> instead of the one that should have been applied, you decided to go ahead and compare the result with results of all the functions you could come up with. Given the variable <code>x</code> and a list of <code>functions</code>, return a list of values <code>f(x)</code> for each <code>x</code> in <code>functions</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>x = 1</code> and<br />
<code>functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]</code>,<br />
the output should be<br />
<code>solution(x, functions) = [0.84147, 0.5403, 2, 1]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] float x</strong></p>
<p>The value to which the functions should be applied. It is guaranteed to have at most <code>1</code> digit after the decimal point.</p>
<p><em>Guaranteed constraints:</em><br />
<code>-1000 ≤ x ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.string functions</strong></p>
<p>Array of functions. Each function is given as a string. It is guaranteed that the result of applying function <code>eval</code> to <code>functions[i]</code> produces a valid function for each <code>i</code>. It is also guaranteed that <code>eval(functions[i])</code> is defined in point <code>x</code> for each <code>i</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ functions.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.float</strong></p>
<p>A list of the same length as <code>functions</code>, where the <code>i<sup>th</sup></code> element is the result of applying the <code>i<sup>th</sup></code> function to <code>x</code>. Your output will be considered correct if its absolute error does not exceed <code>10<sup>-5</sup></code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
