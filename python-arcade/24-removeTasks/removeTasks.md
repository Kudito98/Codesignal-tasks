<p>Today is a good day: it's the <code>k<sup>th</sup></code> year since you started to work at the company, which means you have to have a party today. In order to get home earlier and prepare for the jamboree, you need to get home early. You decided to remove each <code>k<sup>th</sup></code> tasks from your <code>toDo</code> list, since today is your day and you can do whatever you please.</p>
<p>Given the list of task ids in your <code>toDo</code> list, remove each <code>k<sup>th</sup></code> task from it and return the list of remaining tasks.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>k = 3</code> and <code>toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]</code>,<br />
the output should be<br />
<code>solution(k, toDo) = [1237, 2847, 2947, 1, 374827, 22]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ k ≤ 30</code>.</p>
</li>
<li>
<p><strong>[input] array.integer toDo</strong></p>
<p>Ids of the tasks in your to-do list.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ toDo.length ≤ 100</code>,<br />
<code>1 ≤ toDo[i] ≤ 4 · 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
