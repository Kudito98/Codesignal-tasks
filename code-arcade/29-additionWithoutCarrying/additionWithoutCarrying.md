<p>A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.</p>
<p>Given two integers, your task is to find the result that the child will get.</p>
<p><em>Note: The child had learned from <a href="https://www.mathsisfun.com/numbers/addition-column.html" target="_blank">this</a> site, so feel free to check it out too if you are not familiar with column addition</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>param1 = 456</code> and <code>param2 = 1734</code>, the output should be<br />
<code>solution(param1, param2) = 1180</code>.</p>
<pre><code>   456
  1734
+ ____
  1180
</code></pre>
<p>The child performs the following operations from right to left:</p>
<ul>
<li><code>6 + 4 = 10</code> but the child forgets about carrying the <code>1</code> and just writes down the <code>0</code> in the last column</li>
<li><code>5 + 3 = 8</code></li>
<li><code>4 + 7 = 11</code> but the child forgets about the leading <code>1</code> and just writes down <code>1</code> under <code>4</code> and <code>7</code>.</li>
<li>There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that <code>0</code> is written before <code>456</code>. Thus, they get <code>0 + 1 = 1</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer param1</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ param1 &lt; 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer param2</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ param2 &lt; 6 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The result that the little child will get by using column addition without carrying.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
