<p>Given a string which represents a valid arithmetic expression, find the index of the character in the given expression corresponding to the arithmetic operation which needs to be computed first.</p>
<p>Note that several operations of the same type with equal priority are computed from left to right.</p>
<p>See the explanation of the third example for more details about the operations priority in this problem.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>expr = "(2 + 2) * 2"</code>, the output should be<br />
<code>solution(expr) = 3</code>.</p>
<p>There are two operations in the expression: <code>+</code> and <code>*</code>. The result of <code>+</code> should be computed first, since it is enclosed in parentheses. Thus, the output is the index of the <code>'+'</code> sign, which is <code>3</code>.</p>
</li>
<li>
<p>For <code>expr = "2 + 2 * 2"</code>, the output should be<br />
<code>solution(expr) = 6</code>.</p>
<p>There are two operations in the given expression: <code>+</code> and <code>*</code>. Since there are no parentheses, <code>*</code> should be computed first as it has higher priority. The answer is the position of <code>'*'</code>, which is <code>6</code>.</p>
</li>
<li>
<p>For <code>expr = "((2 + 2) * 2) * 3 + (2 + (2 * 2))"</code>, the output should be <code>solution(expr) = 28</code>.</p>
<p>There are two operations which are enclosed in two parentheses: <code>+</code> at the position <code>4</code>, and <code>*</code> at the position <code>28</code>. Since <code>*</code> has higher priority than <code>+</code>, the answer is <code>28</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string expr</strong></p>
<p>A string consisting of digits, parentheses, addition and multiplication signs (pluses and asterisks). It is guaranteed that there is at least one arithmetic sign in it.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ expr.length ≤ 45</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
