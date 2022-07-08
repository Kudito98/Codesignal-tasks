<p>Given integers <code>a</code> and <code>b</code>, determine whether the following pseudocode results in an infinite loop</p>
<pre><code>while a is not equal to b do
  increase a by 1
  decrease b by 1
</code></pre>
<p>Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>a = 2</code> and <code>b = 6</code>, the output should be<br />
<code>solution(a, b) = false</code>;</li>
<li>For <code>a = 2</code> and <code>b = 3</code>, the output should be<br />
<code>solution(a, b) = true</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ a ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ b ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the pseudocode will never stop, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
