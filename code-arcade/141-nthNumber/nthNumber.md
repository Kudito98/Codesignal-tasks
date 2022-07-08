<p>You are given a string <code>s</code> of characters that contains at least <code>n</code> numbers (here, a <em>number</em> is defined as a consecutive series of digits, where any character immediately to the left and right of the series are not digits). The numbers may contain leading zeros, but it is guaranteed that each number has at least one non-zero digit in it.</p>
<p>Your task is to find the <code>n<sup>th</sup></code> number and return it as a string without leading zeros.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>s = "8one 003number 201numbers li-000233le number444"</code> and <code>n = 4</code>,<br />
the output should be<br />
<code>solution(s, n) = "233"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p>A string containing at least <code>n</code> numbers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>20 ≤ s.length ≤ 650</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>1-based index of the number to find.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The <code>n<sup>th</sup></code> number without leading zeros.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
