<p>For the upcoming academic year the Coolcoders University should decide which students will get the scholarships. Scholarships are considered to be <em>correctly distributed</em> if all best students have it, but not all students in the university do. Obviously, only university students should be able to get a scholarship, i.e. there should be no outsiders in the list of the students that will get a scholarships.</p>
<p>You are given lists of unique student ids <code>bestStudents</code>, <code>scholarships</code> and <code>allStudents</code>, representing ids of the best students, students that will get a scholarship and all the students in the university, respectively. Return <code>true</code> if the scholarships are <em>correctly distributed</em> and <code>false</code> otherwise.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>bestStudents = [3, 5]</code>, <code>scholarships = [3, 5, 7]</code>, and<br />
<code>allStudents = [1, 2, 3, 4, 5, 6, 7]</code>, the output should be<br />
<code>solution(bestStudents, scholarships, allStudents) = true</code>;</p>
</li>
<li>
<p>For <code>bestStudents = [3, 5]</code>, <code>scholarships = [3, 5]</code>, and<br />
<code>allStudents = [3, 5]</code>, the output should be<br />
<code>solution(bestStudents, scholarships, allStudents) = false</code>.</p>
<p>All students get a scholarship, which is not correct.</p>
</li>
<li>
<p>For <code>bestStudents = [3]</code>, <code>scholarships = [1, 3, 5]</code>, and<br />
<code>allStudents = [1, 2, 3]</code>, the output should be<br />
<code>solution(bestStudents, scholarships, allStudents) = false</code>.</p>
<p>There's no student with id <code>5</code>, yet somehow he managed to get a scholarship.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer bestStudents</strong></p>
<p>Array of unique elements representing ids of the best students in the university. It is guaranteed that all <code>bestStudents</code> are present in <code>allStudents</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ bestStudents.length ≤ 30</code>,<br />
<code>1 ≤ bestStudents[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.integer scholarships</strong></p>
<p>Array of unique elements representing ids of the students that will get a scholarship.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ scholarships.length ≤ 30</code>,<br />
<code>1 ≤ scholarships[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.integer allStudents</strong></p>
<p>Array of unique elements representing ids of the students that will get a scholarship.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ allStudents.length ≤ 30</code>,<br />
<code>1 ≤ allStudents[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the scholarships are <em>correctly distributed</em> and <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
