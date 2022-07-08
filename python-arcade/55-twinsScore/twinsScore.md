<p>Billy and Mandy are twins, and as such they do everything together. Unfortunately during the finals they were forced to write their exams separately, which explains why they got such low scores. However, they are not too sad about it: since they are twins, it's only natural for them to work together, so they are going to sum up their scores for each exam and show them to their mom.</p>
<p>Given two lists of equal size representing the scores Billy and Mandy got for each exam (<code>b</code> and <code>m</code>, respectively), return a single list containing their combined score.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>b = [22, 13, 45, 32]</code> and <code>m = [28, 41, 13, 32]</code>,<br />
the output should be<br />
<code>solution(b, m) = [50, 54, 58, 64]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer b</strong></p>
<p>The scores Billy got during the finals.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ b.length ≤ 20</code>,<br />
<code>0 ≤ b[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.integer m</strong></p>
<p>The scores Mandy got during the finals.</p>
<p><em>Guaranteed constraints:</em><br />
<code>m.length = b.length</code>,<br />
<code>0 ≤ m[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The total scores the twins got during the finals.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
