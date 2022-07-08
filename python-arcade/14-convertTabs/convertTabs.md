<p>You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.</p>
<p>Implement a function that, given a piece of <code>code</code> and a positive integer <code>x</code> will turn each tabulation character in <code>code</code> into <code>x</code> whitespace characters.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>code = "\treturn False"</code> and <code>x = 4</code>, the output should be</p>
<pre><code>solution(code, x) = "    return False"
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string code</strong></p>
<p>Your piece of code.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ code.length ≤ 1500</code>.</p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>The number of whitespace characters (<code>' '</code>) that should replace each occurrence of the tabulation character (<code>'\t'</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ x ≤ 16</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The given <code>code</code> with tabulation characters expanded according to <code>x</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
