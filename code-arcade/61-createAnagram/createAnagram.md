<p>You are given two strings <code>s</code> and <code>t</code> of the same length, consisting of uppercase English letters. Your task is to find the minimum number of <em>"replacement operations"</em> needed to get some <a href="keyword://anagram" target="_blank">anagram</a> of the string <code>t</code> from the string <code>s</code>. A replacement operation is performed by picking exactly one character from the string <code>s</code> and replacing it by some other character.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>s = "AABAA"</code> and <code>t = "BBAAA"</code>, the output should be<br />
<code>solution(s, t) = 1</code>;</li>
<li>For <code>s = "OVGHK"</code> and <code>t = "RPGUC"</code>, the output should be<br />
<code>solution(s, t) = 4</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ s.length ≤ 35</code>.</p>
</li>
<li>
<p><strong>[input] string t</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>t.length = s.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum number of replacement operations needed to get an anagram of the string <code>t</code> from the string <code>s</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
