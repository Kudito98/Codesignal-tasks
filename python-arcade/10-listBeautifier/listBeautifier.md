<p>Let's call a list <em>beautiful</em> if its first element is equal to its last element, or if a list is empty. Given a list <code>a</code>, your task is to chop off its first and its last element until it becomes <em>beautiful</em>. Implement a function that will make the given <code>a</code> <em>beautiful</em> as described, and return the resulting list as an answer.</p>
<p><em>Hint: one of the features introduced in Python 3 called <a href="https://www.python.org/dev/peps/pep-3132/" target="_blank">extended unpacking</a> could help here.</em></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>a = [3, 4, 2, 4, 38, 4, 5, 3, 2]</code>, the output should be<br />
<code>solution(a) = [4, 38, 4]</code>.</p>
<p>Here's how the answer is obtained:<br />
<code>[3, 4, 2, 4, 38, 4, 5, 3, 2]</code> =&gt; <code>[4, 2, 4, 38, 4, 5, 3]</code> =&gt; <code>[2, 4, 38, 4, 5]</code> =&gt; <code>[4, 38, 4]</code>.</p>
</li>
<li>
<p>For <code>a = [1, 4, -5]</code>, the output should be<br />
<code>solution(a) = [4]</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>A list of integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ a.length ≤ 50</code>,<br />
<code>1 ≤ a[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A <em>beautiful</em> list obtained as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
