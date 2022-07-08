<p>A sentence is considered <em>correct</em> if:</p>
<ul>
<li>it starts with a capital letter;</li>
<li>it ends with a full stop, question mark or exclamation point (<code>'.'</code>, <code>'?'</code> or <code>'!'</code>);</li>
<li>full stops, question marks and exclamation points don't appear anywhere else in the sentence.</li>
</ul>
<p>Given a <code>sentence</code>, return <code>true</code> if it is correct and <code>false</code> otherwise.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>sentence = "This is an example of *correct* sentence."</code>,<br />
the output should be<br />
<code>solution(sentence) = true</code>;</p>
</li>
<li>
<p>For <code>sentence = "!this sentence is TOTALLY incorrecT"</code>,<br />
the output should be<br />
<code>solution(sentence) = false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string sentence</strong></p>
<p>A string without newline characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ sentence.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given <code>sentence</code> is correct, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
