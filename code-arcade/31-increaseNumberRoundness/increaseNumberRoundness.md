<p>Define an integer's <em>roundness</em> as the number of trailing zeroes in it.</p>
<p>Given an integer <code>n</code>, check if it's possible to increase <code>n</code>'s roundness by swapping some pair of its digits.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 902200100</code>, the output should be<br />
<code>solution(n) = true</code>.</p>
<p>One of the possible ways to increase <em>roundness</em> of <code>n</code> is to swap digit <code>1</code> with digit <code>0</code> preceding it: <em>roundness</em> of <code>902201000</code> is <code>3</code>, and <em>roundness</em> of <code>n</code> is <code>2</code>.</p>
<p>For instance, one may swap the leftmost <code>0</code> with <code>1</code>.</p>
</li>
<li>
<p>For <code>n = 11000</code>, the output should be<br />
<code>solution(n) = false</code>.</p>
<p><em>Roundness</em> of <code>n</code> is <code>3</code>, and there is no way to increase it.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>100 ≤ n ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if it's possible to increase <code>n</code>'s roundness, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
