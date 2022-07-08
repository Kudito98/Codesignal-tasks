<p>In computer science, function composition is a mechanism of combining simple functions to build more complicated ones. Here's the deal: your colleague working on the databases implemented a low-level API that you have to deal with, and there's no way for you to update it and make it more sophisticated (or simply useful). Now you need to make a function that will be able to combine low-level functions into a single one using the function composition.</p>
<p>Given two functions <code>f</code> and <code>g</code> that you need to combine and a variable <code>x</code>, return the result of the applying the function to <code>x</code>, i.e. <code>f(g(x))</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>f = "math.log10"</code>, <code>g = "abs"</code>, and <code>x = -100</code>,<br />
the output should be<br />
<code>solution(f, g, x) = 2</code>.</p>
<p><code>math.log10(abs(x)) = log<sub>10</sub>(abs(-100)) = log<sub>10</sub>(100) = 2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string f</strong></p>
<p>A function given as a string. It is guaranteed that the result of applying function <code>eval</code> to <code>f</code> produces a valid function. It is also guaranteed that <code>eval(f)</code> is defined in point <code>x</code>.</p>
</li>
<li>
<p><strong>[input] string g</strong></p>
<p>A function in the same format as <code>f</code>.</p>
</li>
<li>
<p><strong>[input] float x</strong></p>
<p>The argument of the functions. It is guaranteed to have at most <code>1</code> digit after the decimal point.</p>
<p><em>Guaranteed constraints:</em><br />
<code>-1000 ≤ x ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] float</strong></p>
<p>The result of applying composition of functions <code>f</code> and <code>g</code> to <code>x</code>. Your output will be considered correct if its absolute error does not exceed <code>10<sup>-5</sup></code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
