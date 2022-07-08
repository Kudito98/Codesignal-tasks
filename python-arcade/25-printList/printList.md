<p>You were supposed to prepare a presentation about lists in Python, but totally forgot about it. Now that you don't have enough time for it, you decide to show some usage examples instead and say with the poker face that this is how you understood the assignment.</p>
<p>Now you need to implement a function that will display a list in the console. Implement a function that, given a list <code>lst</code>, will return it as a string as follows: <code>"This is your list: <em>lst</em>"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>lst = [1, 2, 3, 4, 5]</code>, the output should be<br />
<code>solution(lst) = "This is your list: [1, 2, 3, 4, 5]"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer lst</strong></p>
<p>A list containing integer values.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ lst.length ≤ 50</code>,<br />
<code>-100 ≤ lst[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string containing information about <code>lst</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
