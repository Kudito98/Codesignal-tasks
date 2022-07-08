<p>Not long ago Greg noticed that he started to forget things, and hurried to the doctor. The doc told him that it was perfectly normal for his age, and wrote down a list of <code>pills</code> that Greg can take in order to improve his memory. He especially recommended one medicine as the most effective one.</p>
<p>Unfortunately Greg forgot which medicine is the most effective, and he feels like he really needs to take them. Greg recalls that the name of the most effective medicine goes in the list somewhere after the very first name that has an even length. Your task is to help Greg: given the list of the <code>pills</code>, return a list of three names that go right after the very first medicine name of the even length.</p>
<p>If there are less than three medicines to return, return empty strings instead of them.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]</code>,<br />
the output should be<br />
<code>solution(pills) = ["Bestmedicen", "Superpillsus", ""]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string pills</strong></p>
<p>Array of medicaments written in Greg's prescription. Each title in the list can consist of English letters, digits and whitespace characters.<br />
It is guaranteed that at least one title in the list has an even length.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ pills.length ≤ 10</code>,<br />
<code>2 ≤ pills[i].length ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A list of <code>3</code> elements.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
