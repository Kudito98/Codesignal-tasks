<p>Consider an arithmetic expression of the form <code>a#b=c</code>. Check whether it is possible to replace <code>#</code> with one of the four signs: <code>+</code>, <code>-</code>, <code>*</code> or <code>/</code> to obtain a correct expression.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>a = 2</code>, <code>b = 3</code>, and <code>c = 5</code>, the output should be<br />
<code>solution(a, b, c) = true</code>.</p>
<p>We can replace <code>#</code> with a <code>+</code> to obtain <code>2 + 3 = 5</code>, so the answer is <code>true</code>.</p>
</li>
<li>
<p>For <code>a = 8</code>, <code>b = 2</code>, and <code>c = 4</code>, the output should be<br />
<code>solution(a, b, c) = true</code>.</p>
<p>We can replace <code>#</code> with a <code>/</code> to obtain <code>8 / 2 = 4</code>, so the answer is <code>true</code>.</p>
</li>
<li>
<p>For <code>a = 8</code>, <code>b = 3</code>, and <code>c = 2</code>, the output should be<br />
<code>solution(a, b, c) = false</code>.</p>
<ul>
<li><code>8 + 3 = 11 ≠ 2</code>;</li>
<li><code>8 - 3 = 5 ≠ 2</code>;</li>
<li><code>8 * 3 = 24 ≠ 2</code>;</li>
<li><code>8 / 3 = 2.(6) ≠ 2</code>.</li>
</ul>
<p>So the answer is <code>false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ b ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer c</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ c ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the desired replacement is possible, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
