<p>Given a string <code>s</code>, determine if it is a <a href="keyword://subsequence" target="_blank">subsequence</a> of a given string <code>t</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>t = "CodeSignal"</code> and <code>s = "CoSi"</code>, the output should be<br />
<code>solution(t, s) = true</code>;</p>
</li>
<li>
<p>For <code>t = "CodeSignal"</code> and <code>s = "cosi"</code>, the output should be<br />
the output should be<br />
<code>solution(t, s) = false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string t</strong></p>
<p>A string consisting of English letters, whitespace characters (<code>' '</code>), digits and punctuation marks (<code>".,?!=*+-"</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ t.length ≤ 500</code>.</p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p>A string consisting of English letters, whitespace characters (<code>' '</code>), digits and punctuation marks (<code>".,?!=*+-"</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ s.length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the <code>s</code> is a <em>subsequence</em> of <code>t</code>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
