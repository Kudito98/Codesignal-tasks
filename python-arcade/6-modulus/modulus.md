<p>It frustrates you more than you'd like to admit that the solution operator in Python can be applied to non-integer values. When you write code, you expect the result of the solution operator to always be an integer, but thanks to Python this isn't always the case.</p>
<p>To fix this, you've decided to write your own solution operator as a function. Your task is to implement a function that, given a number <code>n</code>, returns <code>-1</code> if this number is not an integer and <code>n % 2</code> otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 15</code>, the output should be<br />
<code>solution(n) = 1</code>;</p>
</li>
<li>
<p>For <code>n = 23.12</code>, the output should be<br />
<code>solution(n) = -1</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] numeric n</strong></p>
<p>A non-negative number that can be an <code>int</code>, a <code>float</code>, or a <code>long</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>Return <code>n % 2</code> if <code>n</code> is an integer, otherwise return <code>-1</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
