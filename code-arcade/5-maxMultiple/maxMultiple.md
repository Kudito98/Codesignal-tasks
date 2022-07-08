<p>Given a <code>divisor</code> and a <code>bound</code>, find the largest integer <code>N</code> such that:</p>
<ul>
<li><code>N</code> is divisible by <code>divisor</code>.</li>
<li><code>N</code> is less than or equal to <code>bound</code>.</li>
<li><code>N</code> is greater than <code>0</code>.</li>
</ul>
<p>It is guaranteed that such a number exists.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>divisor = 3</code> and <code>bound = 10</code>, the output should be<br />
<code>solution(divisor, bound) = 9</code>.</p>
<p>The largest integer divisible by <code>3</code> and not larger than <code>10</code> is <code>9</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer divisor</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ divisor ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer bound</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ bound ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The largest integer not greater than <code>bound</code> that is divisible by <code>divisor</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
