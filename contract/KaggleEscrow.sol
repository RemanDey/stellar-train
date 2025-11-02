pragma solidity ^0.8.19;

contract KaggleEscrow {
    address public owner;
    uint256 public challengeCount;

    struct Challenge {
        uint256 rewardWei;
        bool funded;
        mapping(address => bool) paid;
    }

    mapping(uint256 => Challenge) private challenges;

    modifier onlyOwner() {
        require(msg.sender == owner, "only owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function createChallenge(uint256 rewardWei) external onlyOwner returns (uint256) {
        uint256 id = challengeCount++;
        challenges[id].rewardWei = rewardWei;
        return id;
    }

    function fundChallenge(uint256 challengeId) external payable onlyOwner {
        require(msg.value == challenges[challengeId].rewardWei, "send exact amount");
        challenges[challengeId].funded = true;
    }

    function paySolver(uint256 challengeId, address payable solver) external onlyOwner {
        Challenge storage c = challenges[challengeId];
        require(c.funded, "not funded");
        require(!c.paid[solver], "already paid");
        c.paid[solver] = true;
        (bool ok, ) = solver.call{value: c.rewardWei}("");
        require(ok, "transfer failed");
    }
}