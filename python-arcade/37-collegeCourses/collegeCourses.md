<p>John has just entered a college, and should now pick several courses to take. He knows nothing, except that number <code>x</code> is a bad luck for him, which is why he won't even consider courses whose title consist of <code>x</code> letters.</p>
<p>Given a list of <code>courses</code>, remove the courses with titles consisting of <code>x</code> letters and return the result.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>x = 7</code> and<br />
<code>courses = ["Art", "Finance", "Business", "Speech", "History", "Writing", "Statistics"]</code>,<br />
the output should be<br />
<code>solution(x, courses) = ["Art", "Business", "Speech", "Statistics"]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>John's unlucky number.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ x ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] array.string courses</strong></p>
<p>The list of courses.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ courses.length ≤ 50</code>,<br />
<code>3 ≤ courses[i].length ≤ 25</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The courses John should consider.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
